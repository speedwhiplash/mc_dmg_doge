import { NestFactory } from '@nestjs/core';
import { NestExpressApplication } from '@nestjs/platform-express';
import { AppModule } from './app.module';

async function bootstrap() {
	const port: number = parseInt(((process.argv || []).find((arg) => arg.startsWith('--port')) || '').split('=')[1], 10) || 3000;
	const app = await NestFactory.create<NestExpressApplication>(AppModule);
	// app.useStaticAssets(join(__dirname, '..', 'public'));
	// app.setBaseViewsDir(join(__dirname, '..', 'views'));
	await app.listen(port);
	console.log('started on port', port)
}

bootstrap();
