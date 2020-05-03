import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { WorkbooksService } from './workbooks.service';
import { CompareService } from './compare/compare.service';
import { ShellService } from './shell/shell.service';

@Module({
	imports: [],
	controllers: [
		AppController
	],
	providers: [
		AppService,
		WorkbooksService,
		CompareService,
		ShellService
	],
})
export class AppModule {
}
