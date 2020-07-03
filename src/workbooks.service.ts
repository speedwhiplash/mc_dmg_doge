import { Injectable } from '@nestjs/common';
import { AllEquipment } from './interfaces';

const fs = require('fs');

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
	}

	async readArmorStats(): Promise<void> {
		await fs.readFile('./armor_stats.json', "utf8", (err, content) => {
			if (err) {
				console.log('Error reading armor_stats:', err);
				return err;
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
}
