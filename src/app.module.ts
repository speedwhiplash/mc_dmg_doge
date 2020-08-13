import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { WorkbooksService } from './workbooks.service';
import { RunScenarioService } from './compare/run-scenario.service';
import { ShellService } from './shell/shell.service';

@Module({
	imports: [],
	controllers: [
		AppController
	],
	providers: [
		AppService,
		WorkbooksService,
		RunScenarioService,
		ShellService
	],
})
export class AppModule {
}
