import { Body, Controller, Get, Param, Post } from '@nestjs/common';
import { Observable } from 'rxjs';

import { AllEquipment, IBobInputs } from './interfaces';
import { AppService } from './app.service';
import { RunSenarioService } from './compare/run-senario.service';
import { WorkbooksService } from './workbooks.service';
import { totalDefenseScore } from './compare/scenarios/total-defense-score/total-defense-score';

@Controller()
export class AppController {
	constructor(
		private readonly appService: AppService,
		private readonly compareService: RunSenarioService,
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
	bestBuildForScenario(@Body() bobParams: IBobInputs, @Param() params): Observable<any> {
		const filteredStats = this.workbooksService.filterWhitelist(bobParams.whitelist);
		switch (params.type) {
			case 'defense':
				return this.compareService.runScenario(totalDefenseScore, filteredStats, bobParams);
		}
	}
}
