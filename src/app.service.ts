import { Injectable } from '@nestjs/common';
import { ShellService } from './shell/shell.service';
import { WorkbooksService } from './workbooks.service';


@Injectable()
export class AppService {

  constructor(
    private readonly shellService: ShellService,
    private readonly workbooksService: WorkbooksService
  ) {
  }
  
  getHello(): string {
    return 'Hello World!';
  }

  async updateStats() {
    await this.shellService.execShellCommand('rm -f armor_stats.json');
    await this.shellService.execShellCommand('python3 prepare.py');
    this.workbooksService.readArmorStats();
    console.log('reloaded armor-stats')
  }
}