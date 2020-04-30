import { Controller, Get, Post } from '@nestjs/common';
import { AppService } from './app.service';
import { AllEquipment, Boots, Chestplate, Equipment, Helmet, Leggings, Mainhand, Offhand } from './interfaces';
import { WorkbooksService } from './workbooks.service';
const exec = require('child_process').exec;

@Controller()
export class AppController {
	constructor(
		private readonly appService: AppService,
		private readonly workbooksService: WorkbooksService,
	) {

	}

	@Get()
	basicThing() {
		return {message: 'You\'re dumb!'};
	}

	@Get('/update-stats')
	updateStats(): void {
		exec('python3 prepare.py')
	}

	@Get('/equipment')
	equipment():AllEquipment {
		return this.workbooksService.armorStats;
	}

	@Post()
	compare(): object {
		// do all the things
		return {};
	}
}
