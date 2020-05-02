import { Body, Controller, Get, Post } from '@nestjs/common';
import { Observable } from 'rxjs';

import { AllEquipment, BobPostBodyType, BuildIndex, Player } from './interfaces';
import { AppService } from './app.service';
import { CompareService } from './compare/compare.service';
import { WorkbooksService } from './workbooks.service';

const exec = require('child_process').exec;

@Controller()
export class AppController {
	constructor(
		private readonly appService: AppService,
		private readonly compareService: CompareService,
		private readonly workbooksService: WorkbooksService,
	) {
	}

	@Get()
	basicThing() {
		return {message: 'You\'re dumb!'};
	}

	@Get('/update-stats')
	updateStats(): void {
		exec('rm -f armor_stats.json')
		exec('python3 prepare.py')
	}

	@Get('/equipment')
	equipment(): AllEquipment {
		return this.workbooksService.armorStats;
	}

	@Post('/bestOverallBuild')
	bestOverallBuild(@Body() bobParams: BobPostBodyType): Observable<BuildIndex> {
		return this.compareService.bestOverallBuild(this.workbooksService.armorStats, bobParams);
	}
}
