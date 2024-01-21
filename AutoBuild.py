import subprocess
import time

def package_project():
    # Adjust the paths and command based on your Unreal Engine installation and project details
    unreal_path = r'"E:\Unreal Editors\UE_5.3\Engine\Binaries\Win64\UnrealEditor.exe"'
    project_path = r'E:\Work\Projects\GGJ-2024\GGJ2024.uproject'
    output_path = r'E:\Work\Projects\GGJ-2024\Build'

    # Command for packaging the project
    package_command = f'{unreal_path} {project_path} -run=AutomationTool -Script=BuildCookRun ' \
                      f'-nocompileeditor -nop4 -project={project_path} -cook -stage -archive -archivedirectory={output_path} ' \
                      '-package -clientconfig=Development -ueexe=UnrealEditor-Cmd.exe -clean -pak -prereqs -nodebuginfo ' \
                      '-targetplatform=Windows'

    subprocess.run(package_command, shell=True)

if __name__ == "__main__":
    # Set the interval for packaging in seconds (1 hour = 3600 seconds)
    packaging_interval = 3600

    while True:
        package_project()
        print(f"Project packaged. Waiting {packaging_interval} seconds until the next packaging.")
        time.sleep(packaging_interval)
