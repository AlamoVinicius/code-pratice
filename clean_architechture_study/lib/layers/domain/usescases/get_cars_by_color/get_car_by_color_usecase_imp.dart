import 'package:clean_architechture_study/layers/domain/entities/car_entity.dart';
import 'package:clean_architechture_study/layers/domain/usescases/get_cars_by_color/get_car_by_color_usecase.dart';

class GetCarByColorUseCaseImp implements GetCarByColorUseCase {
  // regra de negócio simples apenas por didática
  @override
  CarEntity call(String color) {
    if (color.contains('red')) {
      return CarEntity(plate: "ABC-1234", numberDoors: 4, price: 100000.0);
    } else {
      return CarEntity(plate: "qwe-1234", numberDoors: 4, price: 30000.0);
    }
  }
}

// implementation