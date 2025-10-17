# Image Organization for Algorithms Python Project

This project uses a structured approach to organize images used in Jupyter notebooks.

## Directory Structure

Images are organized in two levels:

1. **Project-wide images**: Located in the root `images/` folder
   - Use for images that are used across multiple notebooks
   - Example: Algorithm visualizations that apply to multiple topics

2. **Topic-specific images**: Located in `src/exercices/[topic]/images/` folders
   - Use for images that are specific to notebooks within a single topic
   - Example: Diagrams for a specific array rotation exercise

## Best Practices

1. **Naming Convention**:
   - Use descriptive names with underscores: `[notebook_name]_[purpose]_[number].png`
   - Example: `rotation_array_diagram_1.png`

2. **Linking in Notebooks**:
   - Use relative paths to make notebooks portable
   - For topic-specific images: `./images/filename.png`
   - For project-wide images: `../../../images/filename.png`

3. **Image Types**:
   - Use PNG for diagrams, screenshots, and most visualizations
   - Use JPEG for photographs (if any)
   - Use SVG for vector graphics when available

4. **Documentation**:
   - Each image folder contains a README.md describing its contents

This structure helps keep images organized and separate from notebook code, making the repository cleaner and easier to maintain.