import { Test, TestingModule } from '@nestjs/testing';
import { TotalDefenseScoreService } from './total-defense-score.service';

describe('TotalDefenseScoreService', () => {
  let service: TotalDefenseScoreService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [TotalDefenseScoreService],
    }).compile();

    service = module.get<TotalDefenseScoreService>(TotalDefenseScoreService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
