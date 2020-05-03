import { Body, Controller, Get, Post } from '@nestjs/common';
import { Observable } from 'rxjs';

import { AllEquipment, BobPostBodyType, BuildIndex } from './interfaces';
import { AppService } from './app.service';
import { CompareService } from './compare/compare.service';
import { WorkbooksService } from './workbooks.service';
import { ShellService } from './shell/shell.service';

const exec = require('child_process').exec;

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
		console.log('reloaded armor-stats')
		return {status: 200, statusText: 'reloaded armor-stats'}
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
