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

@WebServlet("/emp_add_acts")
public class empAddActs extends HttpServlet {
	private static final long serialVersionUID = 1L;

    public empAddActs() {
        super();
        // TODO Auto-generated constructor stub
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html; charset=UTF-8");
		DaoEmp de = new DaoEmp();
		EmpVO vo = new EmpVO();
		int cnt = -1;
		
		String e_id = request.getParameter("e_id");
		String e_name = request.getParameter("e_name");
		String sex = request.getParameter("sex");
		String addr = request.getParameter("addr");

		System.out.println("e_name:"+e_name);
		System.out.println("sex:"+sex);
		System.out.println("addr:"+addr);
		
		vo.setE_id(e_id);
		vo.setE_name(e_name);
		vo.setSex(sex);
		vo.setAddr(addr);
		
		try {
			cnt = de.insertEmp(vo);
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		request.setAttribute("cnt", cnt); 
		System.out.println("cnt:"+cnt);
		
		RequestDispatcher rd = request.getRequestDispatcher("/emp_add_acts.jsp");
		rd.forward(request,response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
