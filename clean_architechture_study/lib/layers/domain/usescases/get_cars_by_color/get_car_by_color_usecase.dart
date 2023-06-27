import 'package:clean_architechture_study/layers/domain/entities/car_entity.dart';

abstract class GetCarByColorUseCase {
  CarEntity call(String color);
}

// contrato
