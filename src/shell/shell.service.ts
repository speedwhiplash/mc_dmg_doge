import { Injectable } from '@nestjs/common';

@Injectable()
export class ShellService {
	/**
	 * Executes a shell command and return it as a Promise.
	 * @param cmd {string}
	 * @return {Promise<string>}
	 */
	execShellCommand(cmd) {
		const exec = require('child_process').exec;
		return new Promise((resolve, reject) => {
			exec(cmd, (error, stdout, stderr) => {
				if (error) {
					console.warn(error);
				}
				resolve(stdout? stdout : stderr);
			});
		});
	}
}
