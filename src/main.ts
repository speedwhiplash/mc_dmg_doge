import { NestFactory } from '@nestjs/core';
import { NestExpressApplication } from '@nestjs/platform-express';
import { AppModule } from './app.module';
import { getAttribute } from './util';

async function bootstrap() {
	const port: number = parseInt(getAttribute('port'), 10) || 3000;
	const app = await NestFactory.create<NestExpressApplication>(AppModule);
	await app.listen(port);
	console.log('started on port', port)
}

bootstrap();
