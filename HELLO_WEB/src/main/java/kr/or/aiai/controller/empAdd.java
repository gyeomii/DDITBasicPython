package kr.or.aiai.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.or.aiai.dao.DaoEmp;
import kr.or.aiai.dao.EmpVO;

@WebServlet("/emp_add")
public class empAdd extends HttpServlet {
	private static final long serialVersionUID = 1L;

    public empAdd() {
        super();
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");
		DaoEmp de = new DaoEmp();
		EmpVO vo = new EmpVO();
		int cnt = 0;
		
		String e_id = request.getParameter("e_id");
		String e_name = request.getParameter("e_name");
		String sex = request.getParameter("sex");
		String addr = request.getParameter("addr");
		
		vo.setE_id(e_id);
		vo.setE_name(e_name);
		vo.setSex(sex);
		vo.setAddr(addr);
		
		try {
			cnt = de.insertEmp(vo);
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		String msg = "";
		if(cnt > 0) {
			msg += cnt + "개의 데이터가 추가되었습니다.";
		}else {
			msg += "데이터 추가 실패";			
		}
		
		request.setAttribute("msg", msg);
		
		RequestDispatcher rd = request.getRequestDispatcher("/emp_add.jsp");
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
