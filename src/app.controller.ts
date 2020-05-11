import { Body, Controller, Get, Param, Post } from '@nestjs/common';
import { Observable } from 'rxjs';

import { AllEquipment, IBobInputs, BuildIndex } from './interfaces';
import { AppService } from './app.service';
import { BuildScores, CompareService } from './compare/compare.service';
import { WorkbooksService } from './workbooks.service';
import { ShellService } from './shell/shell.service';

@Controller()
export class AppController {
	constructor(
		private readonly appService: AppService,
		private readonly compareService: CompareService,
		private readonly shellService: ShellService,
		private readonly workbooksService: WorkbooksService,
	) {
	}

	@Get()
	basicThing() {
		return {message: 'You\'re dumb!'};
	}

	@Get('/update-stats')
	async updateStats() {
		await this.shellService.execShellCommand('rm -f armor_stats.json');
		await this.shellService.execShellCommand('python3 prepare.py');
		this.workbooksService.readArmorStats();
		console.log('reloaded armor-stats')
		return {status: 200, statusText: 'reloaded armor-stats'}
	}

	@Get('/equipment')
	equipment(): AllEquipment {
		return this.workbooksService.armorStats;
	}

	@Post('/bob/:type')
	bestOverallBuild(@Body() bobParams: IBobInputs, @Param() params): Observable<BuildScores> {
		if (params.type === 'defense') {
			return this.compareService.bobDefense(this.workbooksService.armorStats, bobParams);
		}
	}
}
