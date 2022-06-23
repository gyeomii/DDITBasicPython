package application;

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

public class Main8 extends Application {
	Parent root;
	Scene scene;
	Button btn;
	TextField tf1;
	TextField tf2;
	TextArea ta;

	@Override
	public void start(Stage primaryStage) {
		try {
			root = FXMLLoader.load(getClass().getResource("main8.fxml"));
			scene = new Scene(root, 400, 600); // (width, height)
			btn = (Button) scene.lookup("#btn");
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			ta = (TextArea) scene.lookup("#ta");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					shiningStar();
				}
			});
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void shiningStar() {
		int n1 = Integer.parseInt(tf1.getText());
		int n2 = Integer.parseInt(tf2.getText());
		String result = drawStar(n1, n2);
		ta.setText(result);
	}

	public String drawStar(int n1, int n2) {
		String result = "";
		if (n1 < n2) {
			for (int i = n1; i <= n2; i++) {
				for (int j = 1; j <= i; j++) {
					result += "*";
				}
				result += "\n";
			}
		} else if (n1 > n2) {
			for (int i = 1; i <= n1 - n2 + 1; i++) {
				for (int j = n1; j >= i; j--) {
					result += "*";
				}
				result += "\n";
			}
		}
		return result;
	}

	public static void main(String[] args) {
		launch(args);
	}
}