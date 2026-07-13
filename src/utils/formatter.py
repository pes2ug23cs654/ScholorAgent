def print_sources(sources):

    print("\nSources:\n")

    for i, source in enumerate(sources, start=1):

        if isinstance(source, dict):
            print(f"{i}. {source['title']}")
            print(source["url"])
            print()

        else:
            print(source)