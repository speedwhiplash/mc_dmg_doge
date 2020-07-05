import { Body, Controller, Get, Param, Post } from '@nestjs/common';
import { Observable } from 'rxjs';

import { AllEquipment, BuildScores, IBobInputs } from './interfaces';
import { AppService } from './app.service';
import { CompareService } from './compare/compare.service';
import { WorkbooksService } from './workbooks.service';

@Controller()
export class AppController {
	constructor(
		private readonly appService: AppService,
		private readonly compareService: CompareService,
		private readonly workbooksService: WorkbooksService,
	) {
		this.updateStats();
	}

	@Get()
	basicThing() {
		return {message: 'You\'re dumb!'};
	}

	@Get('/update-stats')
	async updateStats() {
		await this.appService.updateStats();
		return {status: 200, statusText: 'reloaded armor-stats'}
	}

	@Get('/equipment')
	equipment(): AllEquipment {
		return this.workbooksService.armorStats;
	}

	@Post('/bob/:type')
	bestOverallBuild(@Body() bobParams: IBobInputs, @Param() params): Observable<BuildScores> {
		if (params.type === 'defense') {
			const filteredStats = this.workbooksService.filterWhitelist(bobParams.whitelist);
			return this.compareService.bobDefense(filteredStats, bobParams);
		}
	}
}
