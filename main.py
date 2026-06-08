import yt_dlp
from tqdm import tqdm
import time

def progress_bar_example():
    """Твой оригинальный код для демонстрации прогресса."""
    total = 0
    for _ in tqdm(range(100), desc="Инициализация", ncols=70, colour="#009FBD"):
        total += 1
        time.sleep(0.02)
    return total

def get_description(url: str) -> str:
    """Извлекает описание видео с YouTube."""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
        'force_generic_extractor': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        description = info.get('description', '')
        if not description:
            return "Описание отсутствует."
        return description

if __name__ == "__main__":
    # Шаг 1: Прогресс-бар (твой код)
    progress_bar_example()

    # Шаг 2: Запрос ссылки
    url = input("Введите ссылку на YouTube видео: ").strip()
    if not url:
        print("Ссылка не введена. Выход.")
        exit(1)

    # Шаг 3: Получение и вывод описания
    print("Получаем описание...")
    try:
        desc = get_description(url)
        print("\n" + "=" * 50)
        print(desc)
        print("=" * 50)
    except Exception as e:
        print(f"Ошибка: {e}")