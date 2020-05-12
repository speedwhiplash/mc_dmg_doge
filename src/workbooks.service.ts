import { Injectable } from '@nestjs/common';
import { AllEquipment } from './interfaces';

const fs = require('fs');
const readline = require('readline');
const { google } = require('googleapis');
const SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'];
const TOKEN_PATH = 'token.json';

@Injectable()
export class WorkbooksService {
	armorStats: AllEquipment = {
		helmet: [],
		chestplate: [],
		leggings: [],
		boots: [],
		offhand: []
	}

	constructor() {
		this.readArmorStats();
	}

	readArmorStats() {
		return fs.readFile('./armor_stats.json', "utf8", (err, content) => {
			if (err) {
				return console.log('Error reading armor_stats:', err);
			}
			const stats_arrays = JSON.parse(content);
			const stats = <AllEquipment>{
				helmet: stats_arrays[0],
				chestplate: stats_arrays[1],
				leggings: stats_arrays[2],
				boots: stats_arrays[3],
				offhand: stats_arrays[4],
			}
			console.log('armor stats loaded from disk cache with:');
			console.log(stats.helmet.length + ' helmet');
			console.log(stats.chestplate.length + ' chestplate');
			console.log(stats.leggings.length + ' leggings');
			console.log(stats.boots.length + ' boot');
			console.log(stats.offhand.length + ' offhand');
			this.armorStats = stats;
		});
	}

	printDocTitle(auth) {
		const docs = google.docs({ version: 'v1', auth });
		docs.documents.get({
			documentId: '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE',
		}, (err, res) => {
			if (err) return console.log('The API returned an error: ' + err);
			console.log(`The title of the document is: ${res.data.title}`);
		});
	}

}
