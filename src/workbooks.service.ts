import { Injectable } from '@nestjs/common';

@Injectable()
export class WorkbooksService {
	constructor() {
	}

	getHello(): string {
		return 'Hello World!';
	}
}
