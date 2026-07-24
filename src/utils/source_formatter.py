def format_sources(sources):

    if not sources:
        return "No sources available."

    lines = []

    for i, source in enumerate(sources, start=1):

        title = source.get("title", "Unknown")
        url = source.get("url", "")

        lines.append(f"{i}. {title} ({url})")

    return "\n".join(lines)