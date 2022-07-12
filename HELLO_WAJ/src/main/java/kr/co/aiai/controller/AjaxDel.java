package kr.co.aiai.controller;

import java.io.IOException;
import java.util.HashMap;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.util.AjaxUtil;
import kr.co.aiai.dao.DaoEmp;
import kr.co.aiai.dao.EmpVO;

@WebServlet("/ajaxdel")
public class AjaxDel extends HttpServlet {
	private static final long serialVersionUID = 1L;

	public AjaxDel() {
		super();
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		DaoEmp de = new DaoEmp();

		String e_id = request.getParameter("e_id");

		try {
			int cnt = de.deleteEmp(e_id);
			HashMap<String, String> hm = new HashMap<String, String>();
			hm.put("cnt", cnt+"");
			AjaxUtil.responseJson(response, hm);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doGet(request, response);
	}

}
