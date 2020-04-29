import { Controller, Get, Post } from '@nestjs/common';
import { AppService } from './app.service';


@Controller()
export class AppController {
	constructor(
		private readonly appService: AppService
	) {
	}

	@Get()
	basicThing() {
		return {message: 'You\'re dumb!'};
	}

	@Post()
	compare(): object {
		// do all the things
		return {};
	}
}
