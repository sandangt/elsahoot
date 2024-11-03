export class LoginFailedException extends Error {

  private static ERROR_MESSAGE = 'Failed to login, please recheck quiz id and enter valid username'

  private constructor(message: string) {
    super(message)
  }

  static default() {
    return new LoginFailedException(this.ERROR_MESSAGE);
  }

}
