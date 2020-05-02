import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { WorkbooksService } from './workbooks.service';
import { CompareService } from './compare/compare.service';

@Module({
	imports: [],
	controllers: [
		AppController
	],
	providers: [
		AppService,
		WorkbooksService,
		CompareService
	],
})
export class AppModule {
}
