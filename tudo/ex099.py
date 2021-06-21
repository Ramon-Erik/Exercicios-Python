def maior(*núms):
    print('-=' * 15)
    print('Analizando os valores passados...')
    m = 0
    for num in núms:
        if num > m:
            m = num
        print(num, end=' ')
    print(f'Foram digitados {len(núms)} ao todo.')
    print(f'O maior valor informado foi {m}')


maior(1, 2, 3, 4)
maior(3, 5, 2, 9, 3, 1, 3)
maior(5, 5)
maior(3, 5)
maior(1)
maior()
