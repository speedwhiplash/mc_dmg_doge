import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { WorkbooksService } from './workbooks.service';

@Module({
	imports: [],
	controllers: [
		AppController
	],
	providers: [
		AppService,
		WorkbooksService
	],
})
export class AppModule {
}
