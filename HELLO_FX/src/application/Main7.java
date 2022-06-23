package application;

import java.util.Random;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class Main7 extends Application {
	Parent root;
	Scene scene;
	Button btn;
	TextField tfUser;
	TextField tfCom;
	TextField tfResult;

	@Override
	public void start(Stage primaryStage) {
		try {
			root = FXMLLoader.load(getClass().getResource("main7.fxml"));
			scene = new Scene(root, 250, 350); // (width, height)
			btn = (Button) scene.lookup("#playButton");
			tfUser = (TextField) scene.lookup("#tfUser");
			tfCom = (TextField) scene.lookup("#tfCom");
			tfResult = (TextField) scene.lookup("#tfResult");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					RSP();
				}
			});
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void RSP() {
		String user = tfUser.getText();
		String com = ComRandom();
		String result = "";
		tfCom.setText(com);
		if (user.equals(com)) {
			result = "비김";
		} else if (user.equals("가위") && com.equals("보")
				|| user.equals("바위") && com.equals("가위")
				|| user.equals("보") && com.equals("바위")) {
			result = "USER 승리";
		} else {
			result = "COM 승리";
		}
		tfResult.setText(result);
	}

	public String ComRandom() {
		String com = "";
		Random rnd = new Random();
		int n = rnd.nextInt(3);
		if (n == 0) {
			com = "가위";
		} else if (n == 1) {
			com = "바위";
		} else {
			com = "보";
		}
		return com;
	}

	public static void main(String[] args) {
		launch(args);
	}
}