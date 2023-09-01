// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::env;
use std::fs::File;
use std::io::Write;
use std::path::Path;
use std::process::Command;
use tauri::api::path::resource_dir;
use std::path::PathBuf;

// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

fn main() {
    // 获取当前可执行文件的路径
    let current_exe_path = env::current_exe().expect("Failed to get current executable path");
    let current_exe_dir = current_exe_path.parent().expect("Failed to get parent directory");

    // 定义外部可执行文件的相对路径
    let relative_exe_path = "main.exe";

    // 构建外部可执行文件的完整路径
    let full_exe_path = current_exe_dir.join(relative_exe_path);

    //如果可执行文件不存在，则将其从嵌入的字节数据中提取出来
    if !Path::new(&full_exe_path).exists() {
        let embedded_exe = include_bytes!("main.exe");

        let mut file = File::create(&full_exe_path).expect("Failed to create executable file");
        file.write_all(embedded_exe).expect("Failed to write executable file");
    }

    // 使用 Command::new 方法创建一个新的命令
    let mut command = Command::new(&full_exe_path);

    // 如果需要，可以添加额外的命令参数
    // command.arg("--option");

    // 启动后台进程
    let _ = command.spawn();


    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
