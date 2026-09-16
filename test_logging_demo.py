import logging
import pytest


log = logging.getLogger(__name__)


def test_logging_simple():
    log.info("Тест начался")
    log.warning("Что-то подозрительное")

    result = 2 + 2
    log.info(f"Результат: {result}")

    assert result == 4
    log.info("Тест закончился")


def test_logging_fail():
    log.info("Проверяем что-то важное")
    log.error("Сейчас упадёт")
    assert 1 + 1 == 3