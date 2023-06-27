class CarEntity {
  String plate;
  int numberDoors;
  double price;

  CarEntity({
    required this.plate,
    required this.numberDoors,
    required this.price,
  });

  double get realPrice => price * numberDoors;
}


// regra de negócio da entidade da aplicação
