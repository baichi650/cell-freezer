# 打包为 `freezer-1.3.exe`

## 作用
本仓库提供了一个启动器 `freezer_1_3_launcher.py`，可用 PyInstaller 打包为 Windows EXE。
EXE 运行后会自动打开内置的 `freezer-1.3.html`（若不存在则打开 `index.html`）。

## Windows 打包步骤
1. 安装 Python 3.10+（建议）
2. 在仓库根目录打开 `cmd` 或 PowerShell
3. 安装 PyInstaller：
   ```bash
   pip install pyinstaller
   ```
4. 运行一键脚本：
   ```bat
   build_exe.bat
   ```
5. 生成文件位置：
   - `dist\freezer-1.3.exe`

## 说明
- 该 EXE 会调用系统默认浏览器打开页面，然后启动器进程结束。
- 页面功能（本地存储、导入导出、自动备份）仍在浏览器中按原逻辑运行。
- 如需“内嵌浏览器窗口”的桌面应用，可以后续改为 Electron 或 pywebview 方案。
