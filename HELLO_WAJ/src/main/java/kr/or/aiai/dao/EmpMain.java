package kr.or.aiai.dao;

import java.util.ArrayList;

public class EmpMain {
	public static void main(String[] args) throws Exception {
		DaoEmp de = new DaoEmp();
		
//		getOne
//		EmpVO vo = de.getOne("1");
//		System.out.println(vo);
//		Select
		ArrayList<EmpVO> list = de.getList();
		for (int i = 0; i < list.size(); i++) {
			EmpVO imsi = list.get(i);
			System.out.println(imsi.getE_name());
		}		
//		Insert
//		EmpVO temp = new EmpVO();
//		temp.setE_id("3");
//		temp.setE_name("3");
//		temp.setSex("3");
//		temp.setAddr("3");
//		
//		int cnt = de.insertEmp(temp);
//		
//		if(cnt > 0) {
//			System.out.println(cnt + "개 데이터 추가 성공");
//		}else {
//			System.out.println("데이터 추가 실패");
//		}
//		Update		
//		EmpVO temp = new EmpVO();
//		temp.setE_id("3");
//		temp.setE_name("4");
//		temp.setSex("4");
//		temp.setAddr("4");
//		
//		int cnt = de.updateEmp(temp);
//		
//		if(cnt > 0) {
//			System.out.println(cnt + "개 데이터 수정 성공");
//		}else {
//			System.out.println("데이터 수정 실패");
//		}
//		Delete
//		int cnt = de.deleteEmp("3");
//		
//		if (cnt > 0) {
//			System.out.println(cnt + "개 데이터 삭제 성공");
//		} else {
//			System.out.println("데이터 삭제 실패");
//		}
	}
}
