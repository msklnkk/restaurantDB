
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Это объект конфигурации Alembic, который предоставляет
# доступ к значениям внутри используемого файла .ini
config = context.config

# Интерпретация конфигурационного файла для логирования Python.
# Эта строка настраивает логгеры.
fileConfig(config.config_file_name)

# Импорт базового класса моделей и установка целевых метаданных
from app.models import Base
target_metadata = Base.metadata

def run_migrations_offline():
    """Запуск миграций в 'оффлайн' режиме."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Запуск миграций в 'онлайн' режиме."""
    # Создание движка SQLAlchemy на основе конфигурации
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        # Отключение пула соединений для миграций
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        # Настройка контекста миграции с активным подключением
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        # Выполнение миграций внутри транзакции
        with context.begin_transaction():
            context.run_migrations()
# Определение режима выполнения миграций (оффлайн или онлайн)
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
