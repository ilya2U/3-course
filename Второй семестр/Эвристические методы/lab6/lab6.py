import random
import numpy as np

n = int(input('Число процессоров '))
m = int(input('Число задач '))
t1 = int(input('Минимальное время процесса '))
t2 = int(input('Максимальное премя процесса '))
osob = int(input('Число особей '))
finalCount = int(input('Количество повторений '))
verCross = int(input('Вероятность кросовера '))
verMut = float(input('Вероятность мутации '))
f = open('./result.txt', 'w')

def selection(population, el):
    index = 0
    while(True):
        index = random.randint(0, len(population) - 1)
        if index == el:
            continue
        else:
            break
    return population[index]

def crossover(parent1, parent2, crossover_max, crossover_min):
    child = parent1[:crossover_min] + parent2[crossover_min:crossover_max] + parent1[crossover_max:]
    f.write('\n   Результат кросовера:\n' + '    '+  '  \t'.join([str(i) for i in child]))
    return child

def mutation(individual, chanse):
    ver = random.randint(0, 100)
    f.write('\n\nвероятность мутации: ' + str(ver))
    # f.write('\nMut ver: ' + str(ver))
    if(ver <= chanse):
        # Берем число
        numIndex = random.randint(0, len(individual) - 1)
        number = individual[numIndex]

        # Переводим в бинарку
        binary_number = bin(number)[2:].zfill(8)

        # Берем индексы битов
        random_index1 = 0
        random_index2 = 0

        while(True):
            random_index1 = random.randint(0, 7)
            random_index2 = random.randint(0, 7)

            if(random_index1 == random_index2):
                continue
            else:
                break

        # Меняем индексы местами
        new_str = ''
        for i in range(len(binary_number)):
            if i == random_index1:
                new_str = new_str + binary_number[random_index2] 
            elif i == random_index2:
                new_str =  new_str + binary_number[random_index1]
            else:
                new_str = binary_number[i]

        # Переводим число обратно в десятичное
        number = int(new_str, 2)

        # Возвращаем в ребенка
        individual[numIndex] = number
        # f.write( '\n' + '\t'.join([str(i[0]) + ' ' + str(i[1]) for i in individual]) + '\n')
    return individual

def raspred_mass(raspred_value, individual, n, initMass):
    zero_mass = [0] * n
    for i in range(len(individual)):
        zero_mass[int(individual[i] / raspred_value)] += initMass[int(individual[i] / raspred_value)][i]
    return zero_mass    

def fitness(individual, raspred_value, n, initMass):
    return max(raspred_mass(raspred_value, individual, n, initMass))

def genetic_algorithm():
    raspred_value = int(256/n)
    counter = 0
    popul_count = 0
    lastMin = 0
    fitness_scores = []

    initMass = [[random.randint(t1, t2) for _ in range(m)] for i in range(n)]

    f.write('Данные:\n' + '\n'.join([" ".join([str(el) for el in i]) for i in initMass]))

    population = [[random.randint(0, 255) for j in range(m)] for i in range(osob)]
    
    f.write('\n\nПопуляция:\n' + '\n'.join([" ".join([str(el) for el in i]) for i in population]))

    fitness_scores = [ fitness(individual, raspred_value=raspred_value, n=n, initMass=initMass) for individual in population]

    f.write('\n\nМаксимальные веса:\n' + ' '.join([str(i) for i in fitness_scores]))

    while True:
        popul_count += 1
        if(counter == finalCount - 1): 
            break

        save_population = population[:]

        for el in range(len(save_population)):
            # Выбираем 2-х родителей
            parent1 = save_population[el][:]
            parent2 = selection(save_population, el)

            f.write('\n  Родитель 1:\n' + '\t'.join([str(i) for i in parent1]))
            f.write('\n  Родитель 2:\n' + '\t'.join([str(i) for i in parent2]))

            # Пройдет ли кроссовер
            ver_cross = random.randint(0, 100)
            
            f.write('\n\nВероятность кроссовера: ' + str(ver_cross))

            #Заранее объявляем детей
            child1 = []
            child2 = []

            # Если прошел выполняем
            if(ver_cross <= verCross):
                crossover_point1 = 0
                crossover_point2 = 0

                while(True):
                    crossover_point1 = random.randint(0, len(parent1) - 1)
                    crossover_point2 = random.randint(0, len(parent1) - 1)
                    if(crossover_point1 == crossover_point2):
                        continue
                    else:
                        break

                cross_max = 0
                cross_min = 0

                if(crossover_point1 > crossover_point2):
                    cross_max = crossover_point1
                    cross_min = crossover_point2
                else: 
                    cross_max = crossover_point2
                    cross_min = crossover_point1

                child1 = crossover(parent1, parent2, cross_max, cross_min)
                child2 = crossover(parent2, parent1, cross_max, cross_min)

            # Иначе дете это те же родители    
            else:
                child1 = parent1
                child2 = parent2

            child1 = mutation(child1, verMut)

            f.write('\nМутация результат:\n' + '\t'.join([str(i) for i in child1]))

            child_fitness1 = fitness(child1, raspred_value=raspred_value, n=n, initMass=initMass)
            child_fitness2 = fitness(child2, raspred_value=raspred_value, n=n, initMass=initMass)

            pic_child = []

            if(child_fitness1 >= child_fitness2):
                pic_child = child2
            else:
                pic_child = child1

            population.append(pic_child)

        fitness_scores = [ fitness(individual, raspred_value=raspred_value, n=n, initMass=initMass) for individual in population]
        f.write('\n\nПопуляция:' + str(popul_count) +'\n')
        f.write('\nКонечные веса:\n' + ' '.join([str(i) for i in fitness_scores]))
        temp = np.array(fitness_scores)
        min_indexes = np.argsort(temp, axis=None)[:osob]
        new_temp = [population[i] for i in min_indexes]

        f.write('\n\nРезультат до чистки:\n' + '\n'.join([" ".join([str(el) for el in i]) for i in population]))
        population = new_temp

        f.write('\n\nРезультат популяции:\n' + '\n'.join([" ".join([str(el) for el in i]) for i in population]))

        if not lastMin == 0 and lastMin == min(fitness_scores):
            counter += 1
        else:
            counter = 0
            lastMin = min(fitness_scores)

    best_individual = min(fitness_scores)
    return best_individual

print(genetic_algorithm())
f.close()