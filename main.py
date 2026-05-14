from module1 import Unit
from module2 import Character  
from module3 import Spell, Fireball, IceLance, LightningBolt

def test_abstract_classes():
    print("Тест 1: Абстрактные классы Unit и Spell...")
    try:
        Unit(1, 2, 3, 4, 5, 6)
        raise AssertionError("Unit не должен создавать экземпляры")
    except TypeError:
        pass

    try:
        Spell("Test", 10, 5)
        raise AssertionError("Spell не должен создавать экземпляры")
    except TypeError:
        pass
    print("Абстрактные классы корректно запрещают создание объектов.")

def test_character_validation():
    print("\nТест 2: Валидация класса персонажа...")
    try:
        Character(10, 10, 10, 10, 10, 10, "necromancer")
        raise AssertionError("Должен возникать ValueError для неизвестного класса")
    except ValueError:
        pass
    print("Некорректный класс отклоняется с ValueError.")

def test_character_formulas():
    print("\n🧪 Тест 3: Формулы HP, урона, защиты и маны...")

    w = Character(10, 10, 10, 10, 10, 10, "warrior")
    assert w.max_health == int(10 * 10 + 10 / 2) == 105
    assert w.damage == int(10 * 2.2 + 10 // 3) == 25
    assert w.defense == int(10 * 1.8 + 10 // 4) == 20
    assert w.mana == int(10 + 10 // 2) == 15

    m = Character(5, 8, 12, 15, 20, 10, "mage")
    assert m.max_health == int(12 * 10 + 5 / 2) == 122
    assert m.damage == int(20 * 2.5 + 15 // 2) == 57
    assert m.defense == int(15 * 1.3 + 20 // 6) == 22
    assert m.mana == int(20 * 3 + 15) == 75

    h = Character(8, 15, 10, 12, 7, 9, "hunter")
    assert h.max_health == int(10 * 10 + 8 / 2) == 104
    assert h.damage == int(15 * 1.9 + 8 // 3) == 30
    assert h.defense == int(15 * 1.6 + 10 // 5) == 26
    assert h.mana == int(15 * 1.5 + 12 // 2) == 28

    print("✅ Все формулы верны. Округление до целого в меньшую сторону работает.")

def test_spell_system():
    print("\nТест 4: Система заклинаний и маны...")
    mage = Character(5, 8, 12, 15, 20, 10, "mage")
    initial_mana = mage.mana

    mage.add_spell(Fireball())
    mage.add_spell(IceLance())
    assert len(mage.spells) == 2
    assert mage.mana == initial_mana

    dmg1 = mage.cast_spell(0)
    assert dmg1 == 35
    assert mage.mana == initial_mana - 15

    dmg2 = mage.cast_spell(1)
    assert dmg2 == 25
    assert mage.mana == initial_mana - 25

    try:
        mage.cast_spell(0)
        raise AssertionError("Должно возникать ValueError при нехватке маны")
    except ValueError:
        pass

    try:
        mage.cast_spell(99)
        raise AssertionError("Должно возникать IndexError при неверном индексе")
    except IndexError:
        pass

    try:
        mage.add_spell("не_заклинание")
        raise AssertionError("Должно возникать TypeError при добавлении не-Spell")
    except TypeError:
        pass

    print("✅ Заклинания добавляются, мана списывается, ошибки обрабатываются корректно.")

def run_all_tests():
    print("=" * 45)
    print("ЗАПУСК ПРОВЕРКИ ИГРЫ ОТ КОТА ВАСИЛИЯ 🐾")
    print("=" * 45)

    tests = [
        test_abstract_classes,
        test_character_validation,
        test_character_formulas,
        test_spell_system
    ]

    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"Ошибка в {test.__name__}: {e}")
            traceback.print_exc()

    print("\n" + "=" * 45)
    if passed == len(tests):
        print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ! ПРОГРАММА ГОТОВА К СДАЧЕ.")
    else:
        print(f"ПРОЙДЕНО {passed} из {len(tests)} тестов. Проверьте game.py.")
    print("=" * 45)

if __name__ == "__main__":
    run_all_tests()