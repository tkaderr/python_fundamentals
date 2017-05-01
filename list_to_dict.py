def list_to_dict(arr1,arr2):
    if len(arr1)!= len(arr2):
        if len(arr1)>len(arr2):
            difference=len(arr1)-len(arr2)
            for i in range(0,difference):
                arr2.append(" ")
            new_dict=zip(arr1,arr2)
            new_dict=dict(new_dict)
            print new_dict
        else:
            difference=len(arr2)-len(arr1)
            for i in range(0,difference):
                arr1.append(" ")
            new_dict=zip(arr2,arr1)
            new_dict=dict(new_dict)
            print new_dict
    else:
        new_dict=zip(arr1,arr2)
        new_dict=dict(new_dict)
        print new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "Bob"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


list_to_dict(favorite_animal,name)
