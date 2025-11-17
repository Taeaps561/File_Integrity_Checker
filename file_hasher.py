import hashlib
import os

def calculate_file_hash(filepath, algorithm='sha256'):
    """
    คำนวณค่า Hash ของไฟล์ที่ระบุโดยใช้อัลกอริทึมที่กำหนด
    :param filepath: Path ไปยังไฟล์
    :param algorithm: อัลกอริทึม Hash (เช่น 'sha256', 'md5')
    :return: ค่า Hash ที่เป็น Hex string หรือ None หากเกิดข้อผิดพลาด
    """
    if not os.path.exists(filepath):
        print(f"❌ ไฟล์ไม่พบ: {filepath}")
        return None

    try:
        # สร้างวัตถุ Hash ตามอัลกอริทึมที่เลือก
        hasher = hashlib.new(algorithm)
        
        # อ่านไฟล์เป็นก้อน (chunk) เพื่อจัดการกับไฟล์ขนาดใหญ่
        chunk_size = 4096
        with open(filepath, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                hasher.update(chunk)
                
        return hasher.hexdigest()
        
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดในการคำนวณ Hash: {e}")
        return None

def compare_files_hash(file1_path, file2_path, algorithm='sha256'):
    """
    เปรียบเทียบค่า Hash ของสองไฟล์
    """
    hash1 = calculate_file_hash(file1_path, algorithm)
    hash2 = calculate_file_hash(file2_path, algorithm)
    
    if hash1 and hash2:
        print("\n--- ผลการเปรียบเทียบ ---")
        print(f"ไฟล์ 1 ({algorithm.upper()}): {hash1}")
        print(f"ไฟล์ 2 ({algorithm.upper()}): {hash2}")
        
        if hash1 == hash2:
            print(f"✅ ไฟล์ทั้งสองมีค่า Hash ตรงกัน: ข้อมูลสมบูรณ์")
            return True
        else:
            print(f"❌ ไฟล์ทั้งสองมีค่า Hash ไม่ตรงกัน: ข้อมูลถูกดัดแปลง (Tampered)")
            return False
    return False

if __name__ == '__main__':
    print("===================================================")
    print("    File Integrity Checker (Basic Hashing Utility)")
    print("===================================================")

    while True:
        mode = input("ต้องการ (1) คำนวณ Hash หรือ (2) เปรียบเทียบไฟล์? (พิมพ์ 'exit' เพื่อออก): ")
        if mode.lower() == 'exit':
            break
        
        algorithm = input("ป้อนอัลกอริทึม Hash (เช่น md5, sha256 - ค่าเริ่มต้น: sha256): ") or 'sha256'
        
        if mode == '1':
            filepath = input("ป้อน Path ของไฟล์ที่ต้องการคำนวณ Hash: ")
            file_hash = calculate_file_hash(filepath, algorithm)
            if file_hash:
                print(f"\n✅ Hash ({algorithm.upper()}): {file_hash}")
        
        elif mode == '2':
            file1 = input("ป้อน Path ของไฟล์ที่ 1: ")
            file2 = input("ป้อน Path ของไฟล์ที่ 2: ")
            compare_files_hash(file1, file2, algorithm)
            
        else:
            print("❌ กรุณาป้อน 1 หรือ 2 เท่านั้น")
            
        print("---------------------------------------------------")