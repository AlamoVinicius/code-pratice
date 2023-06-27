import 'package:clean_architechture_study/layers/domain/repositories/save_favorite_car_repository.dart';

import './save_favorite_car_usecase.dart';
import '../../entities/car_entity.dart';

class SaveFavoriteCarUseCaseImp implements SaveFavoriteCarUseCase {
  // inversão do controle de dependência
  final SaveFavoriteCarRepository _saveFavoriteCarRepository;

  SaveFavoriteCarUseCaseImp(this._saveFavoriteCarRepository);

  @override
  Future<bool> call(CarEntity carEntity) async {
    return await _saveFavoriteCarRepository(carEntity);
  }
}
