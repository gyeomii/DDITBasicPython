package kr.or.aiai.dao;

import java.util.ArrayList;

public class EmpMain {
	public static void main(String[] args) throws Exception {
		DaoEmp de = new DaoEmp();
		ArrayList<EmpVO> list = de.getList();
		for (int i = 0; i < list.size(); i++) {
			EmpVO imsi = list.get(i);
			System.out.println(imsi.getE_name());
		}
		
//		EmpVO empVO = new EmpVO();
//		empVO.setE_id("3");
//		empVO.setE_name("3");
//		empVO.setSex("3");
//		empVO.setAddr("3");
//		
//		int cnt = de.insertEmp(empVO);
//		
//		if(cnt > 0) {
//			System.out.println(cnt + "개 데이터 추가 성공");
//		}else {
//			System.out.println("데이터 추가 실패");
//		}
	}
}
