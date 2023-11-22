import random
n = int(input('Число процессоров '))
m = int(input('Число задач '))
t1 = int(input('Мин процесса '))
t2 = int(input('Макс процесса '))
osob = int(input('Число особей '))
finalCount = int(input('Количество повторений '))
verCross = int(input('Вероятность кросовера '))
verMut = float(input('Вероятность мутации '))
f = open('./result.txt', 'w')

def raspred_mass(raspred_value, individual, n):
    zero_mass = [0] * n
    for i in individual:
        zero_mass[int(i[1] / raspred_value)] += i[0]
    return zero_mass    

def fitness(individual, raspred_value, n):
    return max(raspred_mass(raspred_value, individual, n))

def selection(population):
    return random.sample(population, 2)

def mutation(individual, chanse):
    ver = random.randint(0, 100)
    f.write('\n Вер мутации: ' + str(ver))
    if(ver <=  chanse):
        numIndex = random.randint(0, len(individual) - 1)
        number = individual[numIndex][1]
        binary_number = bin(number)[2:].zfill(8)
        random_index = random.randint(0, 7)
        binary_number = binary_number[:random_index] + str(int(binary_number[random_index]) ^ 1) + binary_number[random_index+1:]
        number = int(binary_number, 2)
        individual[numIndex][1] = number
        f.write( '\n' + '\t'.join([str(i[0]) + ' ' + str(i[1]) for i in individual]) + '\n')
    return individual

def crossover(parent1, parent2, chanse, ver_result, crossover_point):
    if(ver_result <=  chanse):
        child = parent1[:crossover_point] + parent2[crossover_point:]
        f.write('\t'.join([str(i[0]) + ' ' + str(i[1]) for i in child]) + '\n')
        return child

    return parent1

def genetic_algorithm(n):
    
    raspred_value = int(256/n)

    counter = 0
    pupul_count = 0

    lastMin = 0

    initMass = [random.randint(t1, t2) for _ in range(m)]

    f.write("Вес задач: " + ' '.join([str(i) for i in initMass]))

    population = [[[j, random.randint(0, 255)] for j in initMass] for i in range(osob)]

    fitness_scores = []

    while(True):
        pupul_count += 1
        fitness_scores = [ fitness(individual, raspred_value=raspred_value, n=n) for individual in population ]
        f.write("\n     Популяция " + str(pupul_count) +  ":\n" + '\n'.join(['\t'.join([ ' '.join([str(k) for k in population[i][j]]) for j in range(len(population[i]))]) for i in range(len(population))]))
        f.write('\n     Вес популяции:\n' + ' '.join([ str(k)  for k in fitness_scores]))
        min_fitness_score = min(fitness_scores)
        if lastMin == 0 or min_fitness_score  < lastMin:
            counter = 0
            lastMin = min_fitness_score
        else: 
            counter += 1

        if(counter == finalCount - 1): 
            break

        parent1, parent2 = selection(population)
        parant_index = population.index(parent1)
        parant_index2 = population.index(parent2)
        f.write('\nВыбор родителей: ' + str(parant_index+1) + ' ' + str(parant_index2+1))

        ver_result = random.randint(0, 100)
        f.write('\nВер кросовера:\n' + str(ver_result))
        crossover_point = random.randint(0, len(parent1) - 1)
        f.write('\nКросовер в: \n' + str(crossover_point))

        f.write('\nРезультат кросовера:\n')
        child1 = crossover(parent1, parent2, verCross, ver_result, crossover_point)
        child2 = crossover(parent2, parent1, verCross, ver_result, crossover_point)

        f.write('\nВер Мутации:\n')
        child1 = mutation(child1, verMut)

        child_fitness1 = fitness(child1, raspred_value=raspred_value, n=n)
        child_fitness2 = fitness(child2, raspred_value=raspred_value, n=n)
        
        f.write(' Дети:\n' + str(child_fitness1) + ' ' + str(child_fitness2))

        pic = 0
        pic_child = []

        if(child_fitness1 >= child_fitness2):
            pic = child_fitness2
            pic_child = child2
        else:
            pic = child_fitness1
            pic_child = child1

        if(fitness(parent1, raspred_value=raspred_value, n=n) > pic):
            population[parant_index] = pic_child
            

    best_individual = min(fitness_scores)
    return best_individual

print(genetic_algorithm(n))
f.close()