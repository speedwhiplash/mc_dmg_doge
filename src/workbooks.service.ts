import { Injectable } from '@nestjs/common';
import { AllEquipment } from './interfaces';

const fs = require('fs');
const readline = require('readline');
const {google} = require('googleapis');
const SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'];
const TOKEN_PATH = 'token.json';

@Injectable()
export class WorkbooksService {
	armorStats: AllEquipment = {
		helmets: [],
		chestplates: [],
		leggings: [],
		boots: [],
		offhands: [],
		mainhands: []
	}

	constructor() {
		this.readArmorStats();
	}

	readArmorStats() {
		return fs.readFile('./armor_stats.json', "utf8", (err, content) => {
			if (err) {
				this.readRemoteWorkbook(this.printDocTitle);
				return console.log('Error reading armor_stats:', err, ' Generating new data from remote workbook');
			}
			const stats_arrays = JSON.parse(content);
			const stats = <AllEquipment>{
				helmets: stats_arrays[0],
				chestplates: stats_arrays[1],
				leggings: stats_arrays[2],
				boots: stats_arrays[3],
				offhands: stats_arrays[4],
				mainhands: []
			}
			console.log('armor stats loaded from disk cache with:');
			console.log(stats.helmets.length + ' helmets');
			console.log(stats.chestplates.length + ' chestplates');
			console.log(stats.leggings.length + ' leggings');
			console.log(stats.boots.length + ' boots');
			console.log(stats.offhands.length + ' offhands');
			this.armorStats = stats;
		});
	}

	printDocTitle(auth) {
		const docs = google.docs({version: 'v1', auth});
		docs.documents.get({
			documentId: '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE',
		}, (err, res) => {
			if (err) return console.log('The API returned an error: ' + err);
			console.log(`The title of the document is: ${res.data.title}`);
		});
	}

	readRemoteWorkbook(callback): void {
		// Load client secrets from a local file.
		fs.readFile('./mc-dmg-doge-reader.json', (err, content) => {
			console.log('type', JSON.parse(content).type)
			if (err) return console.log('Error loading client secret file:', err);
			// Authorize a client with credentials, then call the Google Docs API.
			this.authorize(JSON.parse(content), callback);
		});
	}

	/**
	 * Create an OAuth2 client with the given credentials, and then execute the
	 * given callback function.
	 * @param {Object} credentials The authorization client credentials.
	 * @param {function} callback The callback to call with the authorized client.
	 */
	private authorize(credentials, callback) {
		const {client_secret, client_id, redirect_uris} = credentials.installed;
		const oAuth2Client = new google.auth.OAuth2(
			client_id, client_secret, redirect_uris[0]);

		// Check if we have previously stored a token.
		fs.readFile(TOKEN_PATH, (err, token) => {
			if (err) return this.getNewToken(oAuth2Client, callback);
			oAuth2Client.setCredentials(JSON.parse(token));
			callback(oAuth2Client);
		});
	}

	/**
	 * Get and store new token after prompting for user authorization, and then
	 * execute the given callback with the authorized OAuth2 client.
	 * @param {google.auth.OAuth2} oAuth2Client The OAuth2 client to get token for.
	 * @param {getEventsCallback} callback The callback for the authorized client.
	 */
	private getNewToken(oAuth2Client, callback) {
		const authUrl = oAuth2Client.generateAuthUrl({
			access_type: 'offline',
			scope: SCOPES,
		});
		console.log('Authorize this app by visiting this url:', authUrl);
		const rl = readline.createInterface({
			input: process.stdin,
			output: process.stdout,
		});
		rl.question('Enter the code from that page here: ', (code) => {
			rl.close();
			oAuth2Client.getToken(code, (err, token) => {
				if (err) return console.error('Error retrieving access token', err);
				oAuth2Client.setCredentials(token);
				// Store the token to disk for later program executions
				fs.writeFile(TOKEN_PATH, JSON.stringify(token), (err) => {
					if (err) console.error(err);
					console.log('Token stored to', TOKEN_PATH);
				});
				callback(oAuth2Client);
			});
		});
	}

}
