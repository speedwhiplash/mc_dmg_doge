import { Body, Controller, Get, Param, Post } from '@nestjs/common';
import { Observable } from 'rxjs';

import { AllEquipment, IBobInputs } from './interfaces';
import { AppService } from './app.service';
import { RunScenarioService } from './compare/run-scenario.service';
import { WorkbooksService } from './workbooks.service';
import { totalDefenseScore } from './compare/scenarios/total-defense-score/total-defense-score';

@Controller()
export class AppController {
	port = ((process.argv || []).find((arg) => arg.startsWith('--port')) || '').split('=')[1] || 3000;
	constructor(
		private readonly appService: AppService,
		private readonly compareService: RunScenarioService,
		private readonly workbooksService: WorkbooksService,
	) {
		this.updateStats();
	}

	@Get()
	basicThing() {
		return {message: 'You\'re dumb!'};
	}

	@Get('/status')
	status() {
		return {status: 200, port: this.port}
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

	@Post('/bob/:scenario')
	bestBuildForScenario(@Body() bobParams: IBobInputs, @Param() params): Observable<any> {
		const filteredStats = this.workbooksService.filterWhitelist(bobParams.whitelist);
		switch (params.scenario) {
			case 'defense':
				return this.compareService.runScenario(totalDefenseScore, filteredStats, bobParams);
		}
	}
}
