import multiprocessing


def process_file(file_path, result_queue):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines_count = sum(1 for line in f)
        result_queue.put(f"{file_path}: {lines_count} lines")
    except FileNotFoundError:
        result_queue.put(f"{file_path}: File not found")


def main():
    file_paths = ["file1.txt", "file2.txt", "file3.txt"]

    result_queue = multiprocessing.Queue()
    processes = []

    for path in file_paths:
        p = multiprocessing.Process(target=process_file, args=(path, result_queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    while not result_queue.empty():
        print(result_queue.get())


if __name__ == "__main__":
    main()
