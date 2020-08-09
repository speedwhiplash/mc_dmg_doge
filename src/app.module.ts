import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { WorkbooksService } from './workbooks.service';
import { RunSenarioService } from './compare/run-senario.service';
import { ShellService } from './shell/shell.service';

@Module({
	imports: [],
	controllers: [
		AppController
	],
	providers: [
		AppService,
		WorkbooksService,
		RunSenarioService,
		ShellService
	],
})
export class AppModule {
}
