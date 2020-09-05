import { Injectable } from '@nestjs/common';
import { AllEquipment, BuildAttributeScores, BuildAttributesScore, BuildIndex, Dictionary, HandheldFields, IBobInputs, IBuild } from '../interfaces';
import { Observable, of } from 'rxjs';
import { oneResult, transformIndexesIntoNames } from './compare-util';

const TOP_NUM_OF_SCORES = 15;

@Injectable()
export class RunSenarioService {
	bestScore = 9;
	bestScores: BuildAttributeScores = {};
	worstBestScore = 10;
	numScores = 0;

	runScenario(scenario: Function, filteredEquipment: AllEquipment, bobStats: IBobInputs): Observable<any> {
		console.time('build');
		this.resetScores();

		let indexes: BuildIndex = {helmet: -1, chestplate: -1, leggings: -1, boots: -1, offhand: -1};
		this.deepCompare(scenario, filteredEquipment, indexes, 0, bobStats);

		this.logBuildScore(this.bestScores, filteredEquipment);
		console.timeEnd('build');

		const resp = transformIndexesIntoNames(this.bestScores, filteredEquipment)
		return of(resp);
	}

	private logBuildScore(scores: BuildAttributeScores, filteredEquipment: AllEquipment) {
		const scoreIndexes = Object.keys(scores).map(score => +score).sort();
		const bestIdx = scoreIndexes[0];
		console.log('bestIdx', bestIdx, scoreIndexes)
		console.log(`
	best score: ${bestIdx}
	best build: 
	${filteredEquipment.boots[scores[bestIdx][0].build.boots].Name}, 
	${filteredEquipment.chestplate[scores[bestIdx][0].build.chestplate].Name},
	${filteredEquipment.helmet[scores[bestIdx][0].build.helmet].Name},
	${filteredEquipment.leggings[scores[bestIdx][0].build.leggings].Name},
	${filteredEquipment.offhand[scores[bestIdx][0].build.offhand].Name}`
		);
	}

	private deepCompare(scenario, filteredEquipment: AllEquipment, indexes: BuildIndex, currentSlot, bobStats: IBobInputs): void {
		const slots = ['helmet', 'chestplate', 'leggings', 'boots', 'offhand'];
		let idx = 0;
		while (idx < filteredEquipment[slots[currentSlot]].length) {
			if (currentSlot === 4) {
				let build = {
					boots: filteredEquipment.boots[indexes.boots],
					chestplate: filteredEquipment.chestplate[indexes.chestplate],
					helmet: filteredEquipment.helmet[indexes.helmet],
					leggings: filteredEquipment.leggings[indexes.leggings],
					offhand: filteredEquipment.offhand[idx],
					player: bobStats.player,
					mainhand: bobStats.mainhand
				}
				this.recordBestScores(this.getScore(scenario, build, bobStats), {...indexes, offhand: idx});
			} else {
				indexes[slots[currentSlot]] = idx;
				this.deepCompare(scenario, filteredEquipment, indexes, currentSlot + 1, bobStats);
			}
			idx = idx + 1;
		}
	}

	private getScore(scenario, build: IBuild, bobStats): BuildAttributesScore {
		let fields = [...Object.keys(HandheldFields), 'Protection'];
		let fieldScore: Dictionary<number> = {};

		fields.forEach(field => fieldScore[field] = oneResult(build, field));
		return scenario(fieldScore, bobStats);
	}

	private resetScores() {
		this.bestScore = 10;
		this.bestScores = {};
		this.numScores = 0;
		this.worstBestScore = 9;
	}

	private recordBestScores(defenseScores: BuildAttributesScore, indexes: BuildIndex) {
		if (this.numScores > TOP_NUM_OF_SCORES || defenseScores.score < this.worstBestScore) {
			// Allow multiple builds for same score
			this.bestScores[defenseScores.score] = [...(this.bestScores[defenseScores.score] || []), {build: indexes, scores: defenseScores}];

			let scores = Object.keys(this.bestScores).map(score => +score).sort();
			delete this.bestScores[scores[TOP_NUM_OF_SCORES]];
			this.worstBestScore = scores[scores.length - 1];
			this.bestScore = scores[0];
		}
	}
}
