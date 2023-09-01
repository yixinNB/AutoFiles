use std::fs;

fn main() {
    //update python release
    let _ = fs::remove_file("target/release/main.exe");
    tauri_build::build()
}
