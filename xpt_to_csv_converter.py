# xpt_to_csv_converter.py
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox


def convert_xpt_to_csv():
    """核心转换功能（用pd.read_sas，安全高效）"""
    # 1. 选择XPT文件
    input_file = filedialog.askopenfilename(
        title="选择XPT文件",
        filetypes=[("SAS XPT Files", "*.xpt"), ("All Files", "*.*")]
    )
    if not input_file:
        return

    # 2. 选择CSV输出路径
    output_file = filedialog.asksaveasfilename(
        title="保存为CSV",
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")]
    )
    if not output_file:
        return

    try:
        # 3. 用pandas直接读取XPT（你之前成功用过的！）
        print(f"正在读取 XPT 文件: {input_file}")
        df = pd.read_sas(input_file, format='xport')

        # 4. 保存为CSV（不保留行索引）
        df.to_csv(output_file, index=False)

        # 5. 成功提示
        print(f"✅ 转换成功！已保存至: {output_file}")
        messagebox.showinfo("成功", f"转换完成！\n已保存至:\n{output_file}")

    except Exception as e:
        # 优化错误提示（针对XPT文件）
        error_msg = str(e)
        if "XPORT" in error_msg:
            error_msg += "\n\n提示：文件可能不是有效的XPT格式（请确认文件来源）"
        messagebox.showerror("转换失败", f"转换失败:\n{error_msg}")


# GUI界面（简洁专业）
if __name__ == "__main__":
    root = tk.Tk()
    root.title("XPT转CSV转换器 v1.0")
    root.geometry("400x200")

    # 安全提示
    tk.Label(
        root,
        text="安全提示：仅用于已脱敏数据！\n真实医疗数据需经伦理审批",
        fg="red",
        justify="center",
        font=("Arial", 10, "bold")
    ).pack(pady=10)

    # 转换按钮
    tk.Button(
        root,
        text="点击选择XPT文件并转换为CSV",
        command=convert_xpt_to_csv,
        bg="#4CAF50",  # 保持绿色背景
        fg="#2E2E2E",  # 从白色改为深灰色（更舒适清晰）
        font=("Arial", 12, "bold"),
        padx=20,
        pady=10
    ).pack(pady=20)

    # 版权信息
    tk.Label(
        root,
        text="© 2025 医学生科研助手 | 本地安全工具 | Author: 李喆 | Email: li_zhe@aliyun.com",
        font=("Arial", 8),
        fg="gray"
    ).pack(side="bottom", pady=10)

    root.mainloop()