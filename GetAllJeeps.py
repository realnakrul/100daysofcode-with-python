cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    result = ', '.join(cars['Jeep'])
    return result

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    result = []
    for c in cars:
        result.append(cars[c][0])
    return result


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    result = []
    for c in cars:
        for m in cars[c]:
            if grep.lower() in m.lower():
                result.append(m)
    return sorted(result)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    for c in cars:
        cars[c] = sorted(cars[c])
    return cars


if __name__ == '__main__':
    print(get_all_jeeps(cars))
    print(get_first_model_each_manufacturer(cars))
    print(get_all_matching_models(cars, 'CO'))
    print(sort_car_models(cars))