import { Test, TestingModule } from '@nestjs/testing';
import { RunSenarioService } from './run-senario.service';
import { AllEquipment, IBobInputs } from '../interfaces';

const armorStats = require('../../armor_stats.json');

describe('CompareService', () => {
	let service: RunSenarioService;

	const rebuildEquipment = (stats_arrays) => {
		return <AllEquipment>{
			helmet: stats_arrays[0],
			chestplate: stats_arrays[1],
			leggings: stats_arrays[2],
			boots: stats_arrays[3],
			offhand: stats_arrays[4],
		}
	}

	beforeEach(async () => {
		const module: TestingModule = await Test.createTestingModule({
			providers: [RunSenarioService],
		}).compile();

		service = module.get<RunSenarioService>(RunSenarioService);
	});

	it('should be defined', () => {
		expect(service).toBeDefined();
	});

	/*it('should compare', (done) => {
		let mockBob = {scenario:{}, player:{}, mainhand:{}} as IBobInputs;
		mockBob.scenario[IScenarioInputs.Damage] = 30;
		mockBob.scenario[EquipmentFields['Hits Taken']] = 1;
		mockBob.scenario[EquipmentFields['Damage Absorbed']] = 100;
		mockBob.scenario[EquipmentFields['Health Regained']] = 0;
		mockBob.scenario[EquipmentFields['Health Regain Percent']] = 0;

		mockBob.player[EquipmentFields.Armor] = 0;
		mockBob.player[EquipmentFields['Armor Percent']] = 100;
		mockBob.player[EquipmentFields.Health] = 20;
		mockBob.player[EquipmentFields['Health Percent']] = 100;
		mockBob.player[EquipmentFields.Toughness] = 0;
		mockBob.player[EquipmentFields['Toughness Percent']] = 100;

		mockBob.mainhand[EquipmentFields.Armor] = 0;
		mockBob.mainhand[EquipmentFields['Armor Percent']] = 0;
		mockBob.mainhand[EquipmentFields.Evasion] = 0;
		mockBob.mainhand[EquipmentFields.Health] = 0;
		mockBob.mainhand[EquipmentFields['Health Percent']] = 0;
		mockBob.mainhand[EquipmentFields.Regeneration] = 0;
		mockBob.mainhand[EquipmentFields.Toughness] = 0;
		mockBob.mainhand[EquipmentFields['Toughness Percent']] = 0;

		service.runScenario(rebuildEquipment(armorStats), mockBob).subscribe(build => {
			expect(rebuildEquipment(armorStats).boots[build.boots].Name).toBe('Winter\'s March');
			expect(rebuildEquipment(armorStats).chestplate[build.chestplate].Name).toBe('Archangel\'s Mail');
			expect(rebuildEquipment(armorStats).helmet[build.helmet].Name).toBe('Frost Giant\'s Crown');
			expect(rebuildEquipment(armorStats).leggings[build.leggings].Name).toBe('Frost Knight\'s Greaves');
			expect(rebuildEquipment(armorStats).offhand[build.offhand].Name).toBe('Embalmer\'s Trophy');
			done();
		});
	})*/
});
